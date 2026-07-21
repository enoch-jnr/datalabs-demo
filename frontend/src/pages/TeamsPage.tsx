import GenericModulePage from "@/components/common/GenericModulePage";

export default function TeamsPage() {
  return (
    <GenericModulePage
      title="Team Management"
      description="Organize people into functional groups within an enterprise."
      apiPath="/teams/"
      columns={[
        { key: "name", label: "Name" },
        { key: "description", label: "Description" },
        { key: "is_active", label: "Active" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "description", label: "Description" },
      ]}
    />
  );
}
