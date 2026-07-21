import { Routes, Route } from "react-router-dom";
import LandingPage from "@/pages/LandingPage";
import LoginPage from "@/pages/auth/LoginPage";
import SignupPage from "@/pages/auth/SignupPage";
import DashboardPage from "@/pages/DashboardPage";
import ProjectsPage from "@/pages/ProjectsPage";
import DatasetsPage from "@/pages/DatasetsPage";
import AnnotationPage from "@/pages/AnnotationPage";
import SearchPage from "@/pages/SearchPage";
import NotificationsPage from "@/pages/NotificationsPage";
import EnterprisesPage from "@/pages/EnterprisesPage";
import TeamsPage from "@/pages/TeamsPage";
import ExperimentsPage from "@/pages/ExperimentsPage";
import ModelRegistryPage from "@/pages/ModelRegistryPage";
import TrainingPage from "@/pages/TrainingPage";
import DeploymentsPage from "@/pages/DeploymentsPage";
import PipelinesPage from "@/pages/PipelinesPage";
import MonitoringPage from "@/pages/MonitoringPage";
import AnalyticsPage from "@/pages/AnalyticsPage";
import PluginsPage from "@/pages/PluginsPage";
import MarketplacePage from "@/pages/MarketplacePage";
import AppLayout from "@/components/layout/AppLayout";
import ProtectedRoute from "@/components/common/ProtectedRoute";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignupPage />} />

      <Route element={<ProtectedRoute />}>
        <Route element={<AppLayout />}>
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/projects" element={<ProjectsPage />} />
          <Route path="/datasets" element={<DatasetsPage />} />
          <Route path="/annotations" element={<AnnotationPage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/notifications" element={<NotificationsPage />} />

          <Route path="/enterprises" element={<EnterprisesPage />} />
          <Route path="/teams" element={<TeamsPage />} />
          <Route path="/experiments" element={<ExperimentsPage />} />
          <Route path="/model-registry" element={<ModelRegistryPage />} />
          <Route path="/training" element={<TrainingPage />} />
          <Route path="/deployments" element={<DeploymentsPage />} />
          <Route path="/pipelines" element={<PipelinesPage />} />
          <Route path="/monitoring" element={<MonitoringPage />} />
          <Route path="/analytics" element={<AnalyticsPage />} />
          <Route path="/plugins" element={<PluginsPage />} />
          <Route path="/marketplace" element={<MarketplacePage />} />
        </Route>
      </Route>
    </Routes>
  );
}
