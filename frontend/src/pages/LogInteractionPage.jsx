import LogInteractionForm from "../components/LogInteractionForm";
import ChatInteraction from "../components/ChatInteraction";
import InteractionSummary from "../components/InteractionSummary";

const LogInteractionPage = () => {
  return (
    <>
      <LogInteractionForm />
      <ChatInteraction />
      <InteractionSummary />
    </>
  );
};

export default LogInteractionPage;
