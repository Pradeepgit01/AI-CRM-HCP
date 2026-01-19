import { useSelector } from "react-redux";

const InteractionSummary = () => {
  const { result, loading } = useSelector((state) => state.interaction);

  if (loading) return <p>Processing interaction...</p>;
  if (!result) return null;

  return (
    <>
      <h3>AI Summary</h3>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </>
  );
};

export default InteractionSummary;
