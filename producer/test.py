import uuid
from rabbitmq import RabbitMQHelper

if __name__ == '__main__':
    rabbitmq = RabbitMQHelper()
    for i in range(100):
        rabbitmq.publish_message("notifications_queue", {
                "job_id": str(uuid.uuid4()),  # Generate a unique job ID
                "title": f"Job Title {i}",
                "company": f"Company {i}",
                "location": "Remote",
                "link": f"https://jobsite.com/job/{i}"
            })

