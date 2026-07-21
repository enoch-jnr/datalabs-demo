import GenericModulePage from "@/components/common/GenericModulePage";

export default function ExperimentsPage() {
  return (
    <GenericModulePage
      title="Experiment Tracking"
      description="Log ML experiment runs, parameters, and metrics as you iterate on models."
      apiPath="/experiments/"
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
