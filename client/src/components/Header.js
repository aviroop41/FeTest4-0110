import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Menu } from '@headlessui/react'; // for dropdown menus
import { FaUserCircle } from 'react-icons/fa'; // user icon

const Header = () => {
    const [theme, setTheme] = useState('light'); // Set default theme to 'mytheme'

    const toggleTheme = () => {
        setTheme(prev => (prev === 'light' ? 'dark' : 'dark')); // Toggle between themes
        document.documentElement.setAttribute('data-theme', theme === 'dark' ? 'dark' : 'dark'); // Apply theme
    };

    return (
        <header className={`bg-base-100 shadow-md p-4 flex justify-between items-center`}>
            <div className="text-xl font-bold">Company Logo</div>
            <input type="text" placeholder="Search..." className="border rounded p-2 shadow" />
            <div className="flex items-center">
                <button onClick={toggleTheme} className="mr-4">Toggle Theme</button>
                <Menu as="div" className="relative">
                    <Menu.Button className="focus:outline-none">
                        <FaUserCircle size={24} />
                    </Menu.Button>
                    <Menu.Items className="absolute right-0 w-48 bg-white shadow-md mt-2 rounded">
                        <Menu.Item>
                            {({ active }) => (
                                <Link to="/profile" className={`block px-4 py-2 text-sm ${active ? 'bg-gray-100' : ''}`}>Profile Settings</Link>
                            )}
                        </Menu.Item>
                        <Menu.Item>
                            {({ active }) => (
                                <Link to="/logout" className={`block px-4 py-2 text-sm ${active ? 'bg-gray-100' : ''}`}>Logout</Link>
                            )}
                        </Menu.Item>
                        <Menu.Item>
                            {({ active }) => (
                                <button onClick={toggleTheme} className={`block px-4 py-2 text-sm ${active ? 'bg-gray-100' : ''}`}>Theme Selection</button>
                            )}
                        </Menu.Item>
                    </Menu.Items>
                </Menu>
            </div>
        </header>
    );
};

export default Header;
