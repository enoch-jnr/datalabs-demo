export interface User {
  id: string;
  email: string;
  username: string | null;
  first_name: string;
  last_name: string;
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
}

export interface Workspace {
  id: string;
  owner_id: string;
  name: string;
  slug: string;
  description: string | null;
  is_active: boolean;
  created_at: string;
}

export interface Project {
  id: string;
  workspace_id: string;
  name: string;
  code: string;
  description: string | null;
  visibility: "PRIVATE" | "WORKSPACE" | "PUBLIC";
  status: "DRAFT" | "ACTIVE" | "ARCHIVED";
  is_active: boolean;
  created_at: string;
}

export interface Dataset {
  id: string;
  project_id: string;
  name: string;
  code: string;
  description: string | null;
  visibility: "PRIVATE" | "PROJECT" | "PUBLIC";
  status: "DRAFT" | "ACTIVE" | "ARCHIVED";
  total_assets: number;
  created_at: string;
}

export interface AnnotationTask {
  id: string;
  project_id: string;
  dataset_id: string | null;
  name: string;
  annotation_type: string;
  status: string;
  created_at: string;
}

export interface AppNotification {
  id: string;
  notification_type: string;
  title: string;
  body: string | null;
  link_url: string | null;
  is_read: boolean;
  created_at: string;
}

export interface SearchResultItem {
  id: string;
  type: string;
  title: string;
  subtitle: string | null;
}
