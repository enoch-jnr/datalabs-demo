import GenericModulePage from "@/components/common/GenericModulePage";

export default function PipelinesPage() {
  return (
    <GenericModulePage
      title="Pipelines"
      description="Chain data processing and ML workflow steps together."
      apiPath="/pipelines/"
      columns={[
        { key: "name", label: "Name" },
        { key: "status", label: "Status" },
        { key: "project_id", label: "Project ID" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "project_id", label: "Project ID" },
      ]}
    />
  );
}
