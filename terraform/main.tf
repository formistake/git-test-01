terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

resource "local_file" "inventario" {
  filename = "${path.module}/inventario.ini"
  content  = <<-EOT
    [web]
    web01 ansible_host=192.168.1.10
  EOT
