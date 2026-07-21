import GenericModulePage from "@/components/common/GenericModulePage";

export default function AnalyticsPage() {
  return (
    <GenericModulePage
      title="Analytics"
      description="Build dashboards to track usage across datasets, annotation, and experiments."
      apiPath="/analytics/dashboards/"
      columns={[
        { key: "name", label: "Name" },
        { key: "project_id", label: "Project ID" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "project_id", label: "Project ID" },
      ]}
    />
  );
}
