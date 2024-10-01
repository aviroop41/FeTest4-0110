import React, { useEffect, useState } from 'react';

// RoleManagement component definition
const RoleManagement = () => {
    const [roles, setRoles] = useState([]);
    const [newRole, setNewRole] = useState({ role_name: '', permissions: [] });
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    // Fetch roles from the server
    useEffect(() => {
        const fetchRoles = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/hr/roles');
                if (!response.ok) throw new Error('Failed to fetch roles');
                const data = await response.json();
                setRoles(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }

        fetchRoles();
    }, []);

    // Handle form input change
    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewRole(prev => ({ ...prev, [name]: value }));
    };

    // Create new role
    const createRole = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:8080/api/hr/roles/create', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(newRole),
            });
            if (!response.ok) throw new Error('Failed to create role');
            const createdRole = await response.json();
            setRoles(prev => [...prev, createdRole]);
            setNewRole({ role_name: '', permissions: [] });
        } catch (error) {
            setError(error.message);
        }
    };

    // Delete role
    const deleteRole = async (role_id) => {
        try {
            const response = await fetch(`http://localhost:8080/api/hr/roles/${role_id}/delete`, { method: 'DELETE' });
            if (!response.ok) throw new Error('Failed to delete role');
            setRoles(prev => prev.filter(role => role.id !== role_id));
        } catch (error) {
            setError(error.message);
        }
    };

    // Update role permissions
    const updatePermissions = async (role_id, permissions) => {
        try {
            const response = await fetch(`http://localhost:8080/api/hr/roles/${role_id}/update`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ permissions }),
            });
            if (!response.ok) throw new Error('Failed to update role');
            const updatedRole = await response.json();
            setRoles(prev => prev.map(role => (role.id === role_id ? updatedRole : role)));
        } catch (error) {
            setError(error.message);
        }
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div className="text-red-500">{error}</div>;

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