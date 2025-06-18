import React, { useState, useEffect } from 'react';

const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchUserData = async () => {
    setLoading(true);
    try {
      const userResponse = await fetch(`/api/users/${userId}`);
      const userData = await userResponse.json();
      setUser(userData);

      const postsResponse = await fetch(`/api/users/${userId}/posts`);
      const postsData = await postsResponse.json();
      setPosts(postsData);
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchUserData();
  }, []); 

  useEffect(() => {
    if (user) {
      document.title = `${user.name} - Profile`;
    }
  }); 

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>{user?.name}</h1>
      <p>{user?.email}</p>
      <h2>Posts ({posts.length})</h2>
      {posts.map(post => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.content}</p>
        </div>
      ))}
    </div>
  );
};
