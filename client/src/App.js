import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import AppPage from './pages/App';

function App() {
  return (
    <Router>
      <Header />
      <nav>
        <Link to="/">Home</Link>
        <Link to="/app">App</Link>
      </nav>
      <Routes>
        <Route path="/app" element={<AppPage />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;