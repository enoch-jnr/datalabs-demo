import GenericModulePage from "@/components/common/GenericModulePage";

export default function DeploymentsPage() {
  return (
    <GenericModulePage
      title="Deployments"
      description="Serve registered models behind endpoints, and monitor their status."
      apiPath="/deployments/"
      columns={[
        { key: "name", label: "Name" },
        { key: "status", label: "Status" },
        { key: "endpoint_url", label: "Endpoint" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "project_id", label: "Project ID" },
      ]}
    />
  );
}
