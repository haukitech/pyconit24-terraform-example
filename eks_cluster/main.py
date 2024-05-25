#!/usr/bin/env python
from cdktf_cdktf_provider_aws.provider import AwsProvider
from constructs import Construct
from cdktf import App, TerraformStack, Token

from imports.eks import Eks
from imports.vpc import Vpc

COMMON_TAGS = {"Environment": "production"}


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "aws", region="eu-central-1")

        my_eks_vpc = Vpc(
            self,
            "MyEksVpc",
            name="my-eks-vpc",
            cidr="10.0.0.0/16",
            azs=["eu-central-1a", "eu-central-1b"],
            private_subnets=["10.0.1.0/24", "10.0.2.0/24"],
            public_subnets=["10.0.101.0/24", "10.0.102.0/24"],
            enable_nat_gateway=True,
            tags=COMMON_TAGS,
        )

        Eks(
            self,
            "MyEks",
            cluster_name="my-eks",
            cluster_version="1.29",
            enable_cluster_creator_admin_permissions=True,
            subnet_ids=Token().as_list(my_eks_vpc.private_subnets_output),
            control_plane_subnet_ids=Token.as_list(my_eks_vpc.public_subnets_output),
            vpc_id=Token().as_string(my_eks_vpc.vpc_id_output),
            cluster_endpoint_public_access=True,
            eks_managed_node_group_defaults={
                "ami_type": "AL2_x86_64",
                "instance_types": ["m5.large"],
            },
            eks_managed_node_groups={
                "default_node_group": {},
            },
            tags=COMMON_TAGS
        )


app = App()
MyStack(app, "cdkexample")

app.synth()
