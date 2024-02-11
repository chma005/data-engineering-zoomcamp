terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.14.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "demo-bucket" {
  name                        = var.gcs_buket_name
  location                    = var.location
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}


# this information comes directly from terraform website. Loads of documentation on how to build terraform files
# resource name = "google_bigquery...", name="demo_dataset"
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}