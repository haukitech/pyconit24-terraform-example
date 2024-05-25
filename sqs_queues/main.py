#!/usr/bin/env python
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.sqs_queue import SqsQueue
from constructs import Construct
from cdktf import App, TerraformStack


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "aws", region="eu-central-1")

        application_queues = ['incoming_messages', 'outgoing_messages']

        for queue in application_queues:
            SqsQueue(
                self,
                queue,
                name=queue.replace("_", "-"),
                delay_seconds=90,
                tags={"Environment": "production"},
            )


app = App()
MyStack(app, "cdkexampl")

app.synth()
