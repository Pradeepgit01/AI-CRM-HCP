import { useDispatch } from "react-redux";
import { logInteraction } from "../redux/interactionSlice";
import { useState } from "react";

const ChatInteraction = () => {
  const [message, setMessage] = useState("");
  const dispatch = useDispatch();

  const sendChat = () => {
    dispatch(
      logInteraction({
        hcp_id: 102,
        rep_id: 1,
        notes: message,
        interaction_type: "chat",
      })
    );
  };

  return (
    <>
      <h3>Chat Interaction</h3>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type chat message"
      />
      <button onClick={sendChat}>Send</button>
    </>
  );
};

export default ChatInteraction;
