# BrighterAI devops task (2022)

You are tasked to deploy the infamous hello-world application to the cloud. The application consists of two pods writing "hello world" to a shared file on a persistent volume.

## Task description

The task is to refactor the deployment structure via the usage of *helm* to an improved state.

Hint: Certain values should be refactored following the *SSOT* (Single Source of Truth) principle. Additionaly, some other values are dependent on the infrastructure and should be injected via environment variables. Keep in mind that in the future the deployment script should work for different clusters (e.g. prod, staging, testing, ...)

## Testing & Deliverable

The task is tailored for azure cloud because a *azure_disk* kubernetes resource is being used. If you should not have azure "at hand" you can replace the *azure_disk* resource with something equivalent of the cloud provider of your choice (AWS, GCP, ...). If you should not have access to any cloud provider it is also fine to deliver an untested solution. Most importantly, we like to see the ideas behind the refactoring, but it doesn't necessarily need to be bug free.

Please deliver the refactored files/folders in a .zip file.
