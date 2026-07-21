import GenericModulePage from "@/components/common/GenericModulePage";

export default function ModelRegistryPage() {
  return (
    <GenericModulePage
      title="Model Registry"
      description="Register trained models, track versions, evaluations, and promote through approval stages."
      apiPath="/models/"
      columns={[
        { key: "name", label: "Name" },
        { key: "stage", label: "Stage" },
        { key: "description", label: "Description" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "project_id", label: "Project ID" },
        { name: "description", label: "Description" },
      ]}
    />
  );
}
