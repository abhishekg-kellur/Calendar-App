// File: src/components/AdminDashboard.js
import React, { useState } from 'react';
import CompanyManagement from './CompanyManagement';
import CommunicationMethods from './CommunicationMethods';
import DashboardOverview from './DashboardOverview';

const AdminDashboard = () => {
  const [activeTab, setActiveTab] = useState('companyManagement');

  return (
    <div className="admin-dashboard">
      <nav className="admin-nav">
        <button onClick={() => setActiveTab('companyManagement')}>Company Management</button>
        <button onClick={() => setActiveTab('communicationMethods')}>Communication Methods</button>
        <button onClick={() => setActiveTab('dashboardOverview')}>Dashboard Overview</button>
      </nav>

      <div className="admin-content">
        {activeTab === 'companyManagement' && <CompanyManagement />}
        {activeTab === 'communicationMethods' && <CommunicationMethods />}
        {activeTab === 'dashboardOverview' && <DashboardOverview />}
      </div>
    </div>
  );
};

export default AdminDashboard;

