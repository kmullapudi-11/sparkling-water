##
## Output variables - used or created resources
##

output "master_public_dns" {
  value = "${aws_emr_cluster.sparkling-water-cluster.master_public_dns}"
}
output "jupyter_url" {
  value = "https://${aws_emr_cluster.sparkling-water-cluster.master_public_dns}:9443"
}