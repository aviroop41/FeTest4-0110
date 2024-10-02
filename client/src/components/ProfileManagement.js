import React, { useEffect, useState } from 'react';

const ProfileManagement = () => {
  const [profile, setProfile] = useState({ name: '', email: '', contact_number: '', address: '' });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const employeeId = 1; // Placeholder for employee ID

  const mockData = [
    { name: 'John Doe', email: 'john@example.com', contact_number: '123-456-7890', address: '123 Main St' },
    { name: 'Jane Smith', email: 'jane@example.com', contact_number: '987-654-3210', address: '456 Elm St' },
    { name: 'Alice Johnson', email: 'alice@example.com', contact_number: '555-555-5555', address: '789 Oak St' },
  ];

  useEffect(() => {
    const fetchProfile = async () => {
      // Mocking the fetch call
      const data = mockData[0]; // Use the first mock data object
      setProfile(data);
      setLoading(false);
    };
    fetchProfile();
  }, [employeeId]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfile((prevProfile) => ({ ...prevProfile, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Mocking the update without error handling
    alert('Profile updated successfully.');
  };

  if (loading) return <p>Loading...</p>;

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md space-y-4">
      <h2 className="text-lg font-bold">Profile Management</h2>
      <div>
        <label htmlFor="name" className="block text-sm font-medium text-gray-700">Name</label>
        <input type="text" name="name" value={profile.name} onChange={handleInputChange} required className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>
      <div>
        <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
        <input type="email" name="email" value={profile.email} onChange={handleInputChange} required className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>
      <div>
        <label htmlFor="contact_number" className="block text-sm font-medium text-gray-700">Contact Number</label>
        <input type="tel" name="contact_number" value={profile.contact_number} onChange={handleInputChange} required className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>
      <div>
        <label htmlFor="address" className="block text-sm font-medium text-gray-700">Address</label>
        <textarea name="address" value={profile.address} onChange={handleInputChange} required className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>
      <button type="submit" className="w-full bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300">Update Profile</button>
    </form>
  );
};

export default ProfileManagement;