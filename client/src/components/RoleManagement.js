import React, { useEffect, useState } from 'react';

// RoleManagement component definition
const RoleManagement = () => {
    const [roles, setRoles] = useState([
        { id: 1, role_name: 'Admin', permissions: ['read', 'write', 'delete'] },
        { id: 2, role_name: 'User', permissions: ['read'] },
        { id: 3, role_name: 'Editor', permissions: ['read', 'write'] },
    ]);
    const [newRole, setNewRole] = useState({ role_name: '', permissions: [] });
    const [loading, setLoading] = useState(false); // Set loading to false for mock data

    // Fetch roles from the server
    useEffect(() => {
        // Mock fetch roles
        setLoading(false);
    }, []);

    // Handle form input change
    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewRole(prev => ({ ...prev, [name]: value }));
    };

    // Create new role
    const createRole = async (e) => {
        e.preventDefault();
        // Mock role creation
        const createdRole = { id: roles.length + 1, ...newRole };
        setRoles(prev => [...prev, createdRole]);
        setNewRole({ role_name: '', permissions: [] });
    };

    // Delete role
    const deleteRole = async (role_id) => {
        // Mock role deletion
        setRoles(prev => prev.filter(role => role.id !== role_id));
    };

    // Update role permissions
    const updatePermissions = async (role_id, permissions) => {
        // Mock role update
        const updatedRole = { ...roles.find(role => role.id === role_id), permissions };
        setRoles(prev => prev.map(role => (role.id === role_id ? updatedRole : role)));
    };

    if (loading) return <div>Loading...</div>;

    return (
        <div className="p-6">
            <h2 className="text-2xl font-bold">Role Management</h2>
            <form onSubmit={createRole} className="mb-4">
                <input
                    type="text"
                    name="role_name"
                    value={newRole.role_name}
                    onChange={handleChange}
                    placeholder="Role Name"
                    className="input w-full mb-2"
                    required
                />
                {/* Permissions can be selected via checkboxes or a dropdown; for simplicity, using input here */}
                <input
                    type="text"
                    name="permissions"
                    value={newRole.permissions}
                    onChange={handleChange}
                    placeholder="Permissions (comma separated)"
                    className="input w-full mb-2"
                />
                <button type="submit" className="btn">Add Role</button>
            </form>
            <ul>
                {roles.map(role => (
                    <li key={role.id} className="flex items-center justify-between mb-2">
                        <div>
                            <strong>{role.role_name}</strong>: {role.permissions.join(', ')}
                        </div>
                        <div>
                            <button onClick={() => updatePermissions(role.id, role.permissions)} className="btn mr-2">Edit</button>
                            <button onClick={() => deleteRole(role.id)} className="btn btn-red">Delete</button>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RoleManagement;