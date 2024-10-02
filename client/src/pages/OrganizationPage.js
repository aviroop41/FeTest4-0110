import React, { useEffect, useState } from 'react'; // Import React and hooks
import OrganizationDirectory from '../components/OrganizationDirectory'; // Import the OrganizationDirectory component
import OrgStructure from '../components/OrgStructure'; // Import the OrgStructure component
import RoleManagement from '../components/RoleManagement'; // Import the RoleManagement component

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
                setEmployees(mockEmployees); // Fallback to mock data if API fails
            } finally {
                setLoading(false); // Set loading to false
            }
        };

        fetchEmployees(); // Call fetch function
    }, []);

    // Render loading indicator or error message if applicable
    if (loading) return <p className="text-center">Loading...</p>; 

    // Render the component
    return (
        <div className="p-4">
            <h1 className="text-3xl font-semibold mb-4">Organization Directory</h1> 
            <OrganizationDirectory employees={employees} /> {/* Pass employees to OrganizationDirectory */}
            <OrgStructure employees={employees} /> {/* Add OrgStructure component for hierarchy visualization */}
            <RoleManagement /> {/* Add RoleManagement component for managing roles */}
        </div>
    );
};

export default OrganizationPage; // Export the component

// Mock API Data Handling (for fallback)
const mockEmployees = [
    { id: 1, name: 'John Doe', position: 'Software Engineer', department: 'Engineering' },
    { id: 2, name: 'Jane Smith', position: 'Product Manager', department: 'Product' },
    { id: 3, name: 'Alice Johnson', position: 'UX Designer', department: 'Design' },
]; // Mock employee data array. 