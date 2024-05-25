# AWS EKS Cluster example

## Prerequisite

Install cdktf

```
~$ npm install --global cdktf-cli
```

Verify the installation

```
~$ cdktf

Commands:
  cdktf deploy [OPTIONS]   Deploy the given stack
  cdktf destroy [OPTIONS]  Destroy the given stack
  cdktf diff [OPTIONS]     Perform a diff (terraform plan) for the given stack
  cdktf get [OPTIONS]      Generate CDK Constructs for Terraform providers and modules.
  cdktf init [OPTIONS]     Create a new cdktf project from a template.
  cdktf login              Retrieves an API token to connect to HCP Terraform.
  cdktf synth [OPTIONS]    Synthesizes Terraform code for the given app in a directory.
```

Install Pipenv

```
~$ brew install pipenv
```

Install Dependency Library

```
~$ pipenv install
```

## Get Started

Generate CDK for Terraform constructs for Terraform provides and modules used in the project.

```
~$ cdktf get
```

Display and analyze a tarraform plan

```
~$ cdktf plan
```

Apply the changes – you need to approve them, once asked.

```bash
cdktf apply
```