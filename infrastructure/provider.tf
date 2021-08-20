provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraforme
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-elvis"
    key    = "state/igti/edc/mod1/terraform.tfstate" #caminho para salvar o arquivo
    region = "us-east-2"
  }
}