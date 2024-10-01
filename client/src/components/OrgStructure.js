import React, { useEffect, useState } from 'react';

const OrgStructure = () => {
    const [orgData, setOrgData] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchOrgStructure = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/organization/structure');
                if (!response.ok) throw new Error('Network response was not ok');
                const data = await response.json();
                setOrgData(data);
            } catch (error) {
                setError('Failed to fetch organization structure. Showing mock data.');
                // Mock data in case of fetch failure
                setOrgData([
                    { id: 1, name: 'Marketing', roles: ['Manager', 'Executive'] },
                    { id: 2, name: 'Development', roles: ['Lead Developer', 'Frontend Developer'] },
                ]);
            }
        };
        fetchOrgStructure();
    }, []);

    return (
        <div className="org-structure-container p-4">
            <h2 className="text-2xl font-semibold mb-4">Organization Structure</h2>
            {error && <div className="error-message text-red-600 mb-2">{error}</div>}
            <div className="org-structure">
                {orgData.map(department => (
                    <div key={department.id} className="department-card bg-white border rounded-lg shadow-md p-4 mb-4">
                        <h3 className="department-name text-xl font-bold">{department.name}</h3>
                        <ul className="roles-list list-disc pl-5">
                            {department.roles.map((role, index) => (
                                <li key={index} className="role-item text-lg">{role}</li>
                            ))}
                        </ul>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default OrgStructure;