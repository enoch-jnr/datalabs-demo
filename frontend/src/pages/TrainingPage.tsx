import GenericModulePage from "@/components/common/GenericModulePage";

export default function TrainingPage() {
  return (
    <GenericModulePage
      title="Training Jobs"
      description="Launch and monitor distributed training runs against your datasets."
      apiPath="/training-jobs/"
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
