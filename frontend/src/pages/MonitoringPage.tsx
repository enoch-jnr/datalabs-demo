import GenericModulePage from "@/components/common/GenericModulePage";

export default function MonitoringPage() {
  return (
    <GenericModulePage
      title="Monitoring"
      description="Track alerts and incidents against live deployments and pipelines."
      apiPath="/monitoring/alerts/"
      columns={[
        { key: "name", label: "Name" },
        { key: "severity", label: "Severity" },
        { key: "message", label: "Message" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "project_id", label: "Project ID" },
        { name: "message", label: "Message" },
      ]}
    />
  );
}
