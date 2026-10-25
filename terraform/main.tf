terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "college_portal" {
  ami                    = "ami-01a00762f46d584a1"
  instance_type          = "t3.micro"
  key_name               = "college-devops-key"
  vpc_security_group_ids = ["sg-0e679c51cc5b01726"]
  subnet_id              = "subnet-0899396ccc5782b4d"

  tags = {
    Name = "college-complaint-portal"
  }

  lifecycle {
    prevent_destroy = true
  }
}
