import LogInteractionForm from "../components/logIteractionForm";
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
