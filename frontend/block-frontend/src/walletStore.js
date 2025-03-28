import { defineStore } from "pinia";
import { ref } from "vue";
import { BrowserProvider } from "ethers"; 
import axios from "axios";

export const useWalletStore = defineStore("wallet", () => {
  const walletAddress = ref(null);
  const authenticated = ref(false);
  const errorMessage = ref("");

  async function connectWallet() {
    if (!window.ethereum) {
      errorMessage.value = "MetaMask is required!";
      return;
    }

    try {
      const provider = new BrowserProvider(window.ethereum);
      await window.ethereum.request({ method: "eth_requestAccounts" });

      const signer = await provider.getSigner();
      walletAddress.value = await signer.getAddress();

      const message = "Sign this message to authenticate";
      const signedMessage = await signer.signMessage(message);

      // Send signed message to backend for verification
      const response = await axios.post("http://127.0.0.1:8000/verify", {
        wallet_address: walletAddress.value,
        signed_message: signedMessage,
      });

      console.log(walletAddress.value);
      console.log(signedMessage);

      if (response.data.message === "Authentication successful") {
        authenticated.value = true;
      }
    } catch (error) {
      errorMessage.value = "Authentication failed!";
      console.error(error);
    }
  }

  return { walletAddress, authenticated, errorMessage, connectWallet };
});
