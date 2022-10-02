import requests
from mailchimp3 import MailChimp
import mailchimp_marketing
from string import Template
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

MC_API = "93d78f46acf71fc5e0a0500ade960cf3-us18"
MC_USERNAME = "Gene Ni"

# you got that dog in you

data = {'Email': 'gni@umd.edu', 'Name': 'Gene Ni'}
list_id = "YOUR_LIST_ID"
audience_id = "d90edc6d37"
member_info = {
    "email_address": "gni@umd.edu",
    "status": "subscribed",
    "merge_fields": {
        "FNAME": "Genesis",
        "LNAME": "Evangelion"
    }
}

try:
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": "93d78f46acf71fc5e0a0500ade960cf3-us18",
        "server": "us18"
    })
    response = client.ping.get()
    print("RHkte;rht'slr")
    print(response)

    body = {
        "permission_reminder": "You signed up for updates on our website",
        "email_type_option": False,
        "campaign_defaults": {
            "from_name": "Mailchimp",
            "from_email": "freddie@mailchimp.com",
            "subject": "Python Developers",
            "language": "EN_US"
        },
        "name": "JS Developers Meetup",
        "contact": {
                "company": "Mailchimp",
                "address1": "675 Ponce de Leon Ave NE",
                "address2": "Suite 5000",
                "city": "Atlanta",
                "state": "GA",
                "zip": "30308",
                "country": "US"
        }
    }
    print("RHkte;rht'slr")
    response = client.lists.create_list({"name": "name", "email_type_option": True, "contact": {"company": "company", "address1": "address1",
                                        "city": "city", "country": "country"}, "campaign_defaults": {"from_name": "from_name", "from_email": "gni@umd.edu", "subject": "subject", "language": "language"}})
    # print(response)
    print("fjk")

    print(client.lists.get_all_lists())

except ApiClientError as error:
    print(error)

# response = MailChimp.lists.create_list(body)
# response = MailChimp.lists.add_list_member(list_id, member_info)
# client.campaigns.send()
