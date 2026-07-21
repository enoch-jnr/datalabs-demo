import GenericModulePage from "@/components/common/GenericModulePage";

export default function PluginsPage() {
  return (
    <GenericModulePage
      title="Plugins"
      description="Manage installed platform extensions."
      apiPath="/plugins/"
      columns={[
        { key: "name", label: "Name" },
        { key: "version", label: "Version" },
        { key: "is_active", label: "Active" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "version", label: "Version", defaultValue: "0.1.0" },
      ]}
    />
  );
}
