import React, { useEffect, useState } from 'react'; // Import React and hooks
import OrganizationDirectory from '../components/OrganizationDirectory'; // Import the OrganizationDirectory component

const OrganizationPage = () => {
    const [employees, setEmployees] = useState([]); // State to store employee data
    const [loading, setLoading] = useState(true); // State to track loading status
    const [error, setError] = useState(null); // State to handle errors

    // Fetch employee data from the API
    useEffect(() => {
        const fetchEmployees = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/organization/directory'); // API call
                if (!response.ok) {
                    throw new Error('Network response was not ok'); // Handle non-200 responses
                }
                const data = await response.json(); // Parse JSON response
                setEmployees(data); // Update state with employee data
            } catch (err) {
                console.error(err);
                setError(err.message); // Handle errors
            } finally {
                setLoading(false); // Set loading to false
            }
        };

        fetchEmployees(); // Call fetch function
    }, []);

    // Render loading indicator or error message if applicable
    if (loading) return <p className="text-center">Loading...</p>; 
    if (error) return <p className="text-red-600 text-center">{error}</p>;

    // Render the component
    return (
        <div className="p-4">
            <h1 className="text-3xl font-semibold mb-4">Organization Directory</h1> 
            <OrganizationDirectory employees={employees} /> {/* Pass employees to OrganizationDirectory */}
        </div>
    );
};

export default OrganizationPage; // Export the component

// OrganizationDirectory Component Implementation

import React from 'react'; // Import React

const OrganizationDirectory = ({ employees }) => {
    return (
        <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                    <tr>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Position</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Department</th>
                    </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    {employees.map((employee) => (
                        <tr key={employee.id}>
                            <td className="px-6 py-4 whitespace-nowrap">{employee.name}</td>
                            <td className="px-6 py-4 whitespace-nowrap">{employee.position}</td>
                            <td className="px-6 py-4 whitespace-nowrap">{employee.department}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default OrganizationDirectory; // Export the component

// Mock API Data Handling (for fallback)

const mockEmployees = [
    { id: 1, name: 'John Doe', position: 'Software Engineer', department: 'Engineering' },
    { id: 2, name: 'Jane Smith', position: 'Product Manager', department: 'Product' },
    { id: 3, name: 'Alice Johnson', position: 'UX Designer', department: 'Design' },
]; // Mock employee data array

// In case of API failure, use mock data
if (employees.length === 0) {
    setEmployees(mockEmployees); // Fallback to mock data
}