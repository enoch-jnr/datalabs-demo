import GenericModulePage from "@/components/common/GenericModulePage";

export default function MarketplacePage() {
  return (
    <GenericModulePage
      title="Marketplace"
      description="Browse and publish plugins, datasets, and models for the community."
      apiPath="/marketplace/items/"
      columns={[
        { key: "name", label: "Name" },
        { key: "item_type", label: "Type" },
        { key: "price_cents", label: "Price (cents)" },
      ]}
      createFields={[
        { name: "name", label: "Name" },
        { name: "item_type", label: "Type (PLUGIN/DATASET/MODEL)" },
        { name: "price_cents", label: "Price (cents)", type: "number", defaultValue: "0" },
      ]}
    />
  );
}
