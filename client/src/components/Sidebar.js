import React from 'react';
import { NavLink } from 'react-router-dom';
import { FaHome, FaTachometerAlt, FaUser, FaPeopleArrows, FaBuilding, FaUserCircle } from 'react-icons/fa'; // Importing relevant icons

const Sidebar = () => {
  return (
    <aside className="w-64 h-full bg-gray-100 p-4 fixed">
      <h2 className="text-lg font-bold mb-4">Navigation</h2>
      <ul className="space-y-2">
        <li>
          <NavLink to="/" 
                   className={({ isActive }) => `flex items-center p-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-blue-200'} transition-all duration-200 ease-in-out`}>
            <FaHome className="mr-3" /> Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/app" 
                   className={({ isActive }) => `flex items-center p-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-blue-200'} transition-all duration-200 ease-in-out`}>
            <FaTachometerAlt className="mr-3" /> App
          </NavLink>
        </li>
        <li>
          <NavLink to="/dashboard" 
                   className={({ isActive }) => `flex items-center p-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-blue-200'} transition-all duration-200 ease-in-out`}>
            <FaUser className="mr-3" /> Dashboard
          </NavLink>
        </li>
        <li>
          <NavLink to="/me" 
                   className={({ isActive }) => `flex items-center p-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-blue-200'} transition-all duration-200 ease-in-out`}>
            <FaUserCircle className="mr-3" /> Me
          </NavLink>
        </li>
        <li>
          <NavLink to="/my-team" 
                   className={({ isActive }) => `flex items-center p-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-blue-200'} transition-all duration-200 ease-in-out`}>
            <FaPeopleArrows className="mr-3" /> My Team
          </NavLink>
        </li>
        <li>
          <NavLink to="/organization" 
                   className={({ isActive }) => `flex items-center p-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-blue-200'} transition-all duration-200 ease-in-out`}>
            <FaBuilding className="mr-3" /> Organization
          </NavLink>
        </li>
        <li>
          <NavLink to="/profile" 
                   className={({ isActive }) => `flex items-center p-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-blue-200'} transition-all duration-200 ease-in-out`}>
            <FaUser className="mr-3" /> Profile
          </NavLink>
        </li>
      </ul>
    </aside>
  );
};

export default Sidebar;