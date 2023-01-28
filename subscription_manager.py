import stripe

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

# create the subscription plan
plan = stripe.Plan.create(
  amount=2999,
  interval='month',
  name='WORMIEsignals Monthly Subscription',
  currency='usd',
  id='wormie-monthly-subscription'
)

# create the annual plan
annual_plan = stripe.Plan.create(
  amount=2879.20,
  interval='year',
  name='WORMIEsignals Annual Subscription',
  currency='usd',
  id='wormie-annual-subscription'
)

# create a customer
def create_customer(email, source):
    customer = stripe.Customer.create(
        email=email,
        source=source
    )
    return customer

# create a subscription for a customer
def create_subscription(customer_id, plan_id):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[
            {
                "plan": plan_id,
            },
        ]
    )
    return subscription

# cancel a subscription
def cancel_subscription(subscription_id):
    subscription = stripe.Subscription.retrieve(subscription_id)
    subscription.delete()
    return subscription

# check if a customer has an active subscription
def check_active_subscription(customer_id):
    subscriptions = stripe.Subscription.list(customer=customer_id)
    for subscription in subscriptions['data']:
        if subscription['status'] == 'active':
            return True
    return False

