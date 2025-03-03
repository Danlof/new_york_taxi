variable "project" {
  description = "Project name"
  default     = "taxi-ny-449314"
}


variable "location" {
  description = "bucket location"
  default     = "US"

}
variable "credentials" {
  description = "my credentials"
  default = "./terrademo/keys/ny-creds.json"
}

variable "region" {
  description = "bucket region"
  default     = "us-central1"

}

variable "bq_dataset_name" {
  description = "My Bigquery Dataset Name"
  default     = "ny_dataset"
}
variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}
variable "gcs_bucket_name" {
  description = "Bucket name"
  default     = "taxi-ny-449314-bucket"
}

