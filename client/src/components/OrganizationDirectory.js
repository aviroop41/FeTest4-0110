import React, { useEffect, useState } from 'react';

const OrganizationDirectory = () => {
    const [employees, setEmployees] = useState([
        { id: 1, name: 'John Doe', role: 'Developer', department: 'Engineering' },
        { id: 2, name: 'Jane Smith', role: 'HR Manager', department: 'Human Resources' },
        { id: 3, name: 'Alice Johnson', role: 'Product Owner', department: 'Product' }
    ]);

    useEffect(() => {
        const fetchEmployees = async () => {
            // Mock data used directly
            setEmployees([
                { id: 1, name: 'John Doe', role: 'Developer', department: 'Engineering' },
                { id: 2, name: 'Jane Smith', role: 'HR Manager', department: 'Human Resources' },
                { id: 3, name: 'Alice Johnson', role: 'Product Owner', department: 'Product' }
            ]);
        };
        
        fetchEmployees();
    }, []);

    return (
        <div className="overflow-x-auto">
            <table className="min-w-full bg-white text-left border border-gray-200">
                <thead>
                    <tr className="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
                        <th className="py-3 px-6">Name</th>
                        <th className="py-3 px-6">Role</th>
                        <th className="py-3 px-6">Department</th>
                    </tr>
                </thead>
                <tbody className="text-gray-600 text-sm font-light">
                    {employees.map(employee => (
                        <tr key={employee.id} className="hover:bg-gray-100">
                            <td className="py-3 px-6">{employee.name}</td>
                            <td className="py-3 px-6">{employee.role}</td>
                            <td className="py-3 px-6">{employee.department}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default OrganizationDirectory;