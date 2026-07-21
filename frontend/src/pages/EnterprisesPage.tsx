import GenericModulePage from "@/components/common/GenericModulePage";

export default function EnterprisesPage() {
  return (
    <GenericModulePage
      title="Enterprise Management"
      description="Create organizations, and (once wired up) invite members, configure features, and review audit logs."
      apiPath="/enterprises/"
      columns={[
        { key: "name", label: "Name" },
        { key: "code", label: "Code" },
        { key: "industry", label: "Industry" },
        { key: "is_active", label: "Active" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "code", label: "Code" },
        { name: "industry", label: "Industry" },
      ]}
    />
  );
}
