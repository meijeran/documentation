---
id: Fluent-Bit
title: Fluent Bit
sidebar_position: 1
overview: Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources. Helm is a tool for managing packages of pre-configured Kubernetes resources using Charts. You can use this Helm chart to ship Kubernetes logs to Logz.io with Fluent Bit. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---



Fluent Bit is an open source Log Processor and Forwarder which allows you to collect any data like metrics and logs from different sources. Helm is a tool for managing packages of pre-configured Kubernetes resources using Charts. You can use this Helm chart to ship Kubernetes logs to Logz.io with Fluent Bit. 


:::note
This chart is based on the [fluent-bit](https://github.com/fluent/helm-charts/tree/main/charts/fluent-bit) Helm chart.
:::
 

###### Sending logs from nodes with taints

If you want to ship logs from any of the nodes that have a taint, make sure that the taint key values are listed in your in your daemonset/deployment configuration as follows:
  
```yaml
tolerations:
- key: 
  operator: 
  value: 
  effect: 
```
  
To determine if a node uses taints as well as to display the taint keys, run:
  
```
kubectl get nodes -o json | jq ".items[]|{name:.metadata.name, taints:.spec.taints}"
```

###### Enabling multiline logs parser

If you want to enable parsing for multiline logs, add the following code to `values.yaml` under the `customParsers` parameter:
  
```yaml
customParsers:
  [MULTILINE_PARSER]
      name          multiline-regex-test
      type          regex
      flush_timeout 1000
```


#### Standard configuration

 

##### Add `logzio-helm` repo
  
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```


###### Run the Helm deployment code

```shell
helm install  \
--set logzio.token=<<LOG-SHIPPING-TOKEN>> \
--set logzio.listenerHost=<<LISTENER-HOST>> \
--set logzio.logType=<<LOG-TYPE>> \
logzio-fluent-bit logzio-helm/logzio-fluent-bit
```
  
{@include: ../_include/log-shipping/listener-var.html} {@include: ../_include/log-shipping/log-shipping-token.html} If required, replace `<<LOG_TYPE>>` with the desired name for the log type, the default value is `fluentbit`.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).

 


####  Customizing Helm chart parameters


##### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`

* Edit the `values.yaml`

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

###### Example

```
helm install logzio-fluent-bit logzio-helm/logzio-fluent-bit -f my_values.yaml 
```

To modify fluentbit configuration, edit the `config` section in `values.yaml`.

#### Uninstalling the Chart

The Uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-fluent-bit` deployment, use the following command:

```shell
helm uninstall logzio-fluent-bit
```