import { useDispatch } from "react-redux";
import { logInteraction } from "../redux/interactionSlice";
import { useState } from "react";

const LogInteractionForm = () => {
  const dispatch = useDispatch();
  const [notes, setNotes] = useState("");

  const submitHandler = () => {
    dispatch(
      logInteraction({
        hcp_id: 101,
        rep_id: 1,
        notes,
        interaction_type: "in-person",
      })
    );
  };

  return (
    <>
      <h3>Structured Interaction</h3>
      <textarea
        rows="4"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        placeholder="Enter interaction details"
      />
      <br />
      <button onClick={submitHandler}>Log Interaction</button>
    </>
  );
};

export default LogInteractionForm;
