import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import AppPage from './pages/App';
import DashboardPage from './pages/DashboardPage';
import MePage from './pages/MePage';

function App() {
  return (
    <Router>
      <Header />
      <nav>
        <Link to="/">Home</Link>
        <Link to="/app">App</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/me">Me</Link>
      </nav>
      <Routes>
        <Route path="/app" element={<AppPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/me" element={<MePage />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;