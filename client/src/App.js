import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import AppPage from './pages/App';
import DashboardPage from './pages/DashboardPage';
import MePage from './pages/MePage';
import MyTeamPage from './pages/MyTeamPage';
import OrganizationPage from './pages/OrganizationPage';
import ProfilePage from './pages/ProfilePage';
import Sidebar from './components/Sidebar';

function App() {
  return (
    <Router>
      <Header />
      {/* <Sidebar /> */}
      <nav className="flex space-x-4 p-4 bg-gray-100 rounded shadow">
        <Link to="/dashboard" className="tab">Dashboard</Link>
        <Link to="/me" className="tab">Me</Link>
        <Link to="/my-team" className="tab">My Team</Link>
        <Link to="/organization" className="tab">Organization</Link>
        <Link to="/profile" className="tab">Profile</Link>
      </nav>
      <Routes>
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/me" element={<MePage />} />
        <Route path="/my-team" element={<MyTeamPage />} />
        <Route path="/organization" element={<OrganizationPage />} />
        <Route path="/profile" element={<ProfilePage />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;