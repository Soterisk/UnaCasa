from django.shortcuts import render, redirect
from django.contrib import messages

from PropertyApp.forms import PropertyForm
from .forms import ReferralForm
from UserApp.models import Agent
from django.contrib.auth import get_user_model
from django.db import transaction

from .models import ReferralImage


def create_referral(request):
    if request.method == 'POST':
        referral_form = ReferralForm(request.POST, request.FILES)
        property_form = PropertyForm(request.POST, request.FILES)
        if referral_form.is_valid() and property_form.is_valid():
            agent_email = referral_form.cleaned_data['agent_email']
            agent_contact_number = referral_form.cleaned_data['agent_contact_number']

            # Check if the user is trying to refer their own property
            if request.user.email == agent_email:
                messages.error(request, "You cannot refer your own property as you're not the landlord.")
                # Render the same form back to the user with the error message
                return render(request, 'refer_property.html', {'form': referral_form})

            User = get_user_model()
            with transaction.atomic():
                # Attempt to get or create a CustomUser for the agent
                user, created = User.objects.get_or_create(email=agent_email, defaults={'username': agent_email, 'tel_num': agent_contact_number})

                if created:
                    user.is_agent = True
                    #send email to confirm?
                    user.email_confirmed = False
                    user.save()

                # Now, ensure the Agent instance is linked to this user
                agent, agent_created = Agent.objects.get_or_create(user=user, defaults={'contact_number': agent_contact_number})

                # Add logic here to actually create/save the referral with all necessary information
                # For example, referral_instance = Referral.objects.create(...)
                # Property handling
                property_instance = property_form.save(commit=False)
                property_instance.agent = agent
                property_instance.save()

                # Referral handling
                referral_instance = referral_form.save(commit=False)
                referral_instance.user = request.user
                referral_instance.property = property_instance
                referral_instance.agent_email = agent_email
                referral_instance.save()

                # Handle referral images if there are any
                for file in request.FILES.getlist('images'):
                    ReferralImage.objects.create(image=file, referral=referral_instance)

            # If everything goes well, redirect to a success URL
            messages.success(request, "Referral created successfully.")
            return redirect('some_success_url')
    else:
        form = ReferralForm()

    # For GET requests or if form is not valid, render the form template
    return render(request, 'refer_property.html', {'form': form})