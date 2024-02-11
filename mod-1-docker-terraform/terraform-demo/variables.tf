variable "credentials" {
  description = "My Credentials"
  default     = "./keys/mycreds.json"
}

variable "project" {
  description = "Project"
  default     = "terraform-demo-412915"
}

variable "region" {
  description = "region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"

}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"

}

variable "gcs_buket_name" {
  description = "My Storage Bucket Name"
  default     = "terraform-demo-412915-terra-bucket"

}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}