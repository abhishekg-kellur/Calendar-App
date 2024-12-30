// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./components/HomePage";
import AdminLogin from "./components/AdminDashboard";
import UserLogin from "./components/UserLogin"; 
import AnalyticsLogin from "./components/AnalyticsLogin";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/admin-login" element={<AdminLogin />} />
        <Route path="/user-login" element={<UserLogin />} />
        <Route path="/analytics-login" element={<AnalyticsLogin />} />
      </Routes>
    </Router>
  );
}

export default App;
