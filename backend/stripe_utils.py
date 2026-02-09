import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_checkout_session(email, price_id):
    return stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": price_id,
            "quantity": 1,
        }],
        success_url="https://yourfrontend.com?success=true",
        cancel_url="https://yourfrontend.com?canceled=true",
        customer_email=email
    )
