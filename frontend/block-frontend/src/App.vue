<template>
  <div class="min-h-screen flex flex-col bg-gray-900 text-white">
    <!-- Navbar -->
    <nav class="bg-gray-800 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-xl font-bold">Web3 Auth</h1>
        <div v-if="walletStore.authenticated">
          <span class="text-sm">🔗 {{ shortWallet }}</span>
          <button @click="logout" class="ml-4 px-4 py-2 bg-red-600 rounded-lg hover:bg-red-500">
            Logout
          </button>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow flex items-center justify-center">
      <div class="p-6 bg-gray-800 rounded-xl text-center" v-if="!walletStore.authenticated">
        <h1 class="text-xl font-bold">Ethereum Authentication</h1>
        
        <p v-if="walletStore.walletAddress" class="mt-2">
          Connected Wallet: <strong>{{ walletStore.walletAddress }}</strong>
        </p>

        <button
          @click="walletStore.connectWallet"
          class="mt-4 px-4 py-2 bg-blue-600 rounded-lg hover:bg-blue-500"
        >
          Connect MetaMask
        </button>

        <p v-if="walletStore.errorMessage" class="mt-2 text-red-500">{{ walletStore.errorMessage }}</p>
      </div>

      <!-- Profile View -->
      <div class="p-6 bg-gray-800 rounded-xl text-center" v-else>
        <h1 class="text-xl font-bold">Profile</h1>
        <p class="mt-2">Welcome, <strong>{{ walletStore.walletAddress }}</strong></p>
        <p class="mt-4 text-green-400">✅ Authenticated</p>
      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 p-4 text-center text-sm">
      <p>© 2025 Web3 Auth. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useWalletStore } from "./walletStore";

const walletStore = useWalletStore();

// Shorten wallet address for display
const shortWallet = computed(() => {
  if (!walletStore.walletAddress) return "";
  return `${walletStore.walletAddress.slice(0, 6)}...${walletStore.walletAddress.slice(-4)}`;
});

// Logout function
const logout = () => {
  walletStore.authenticated = false;
  walletStore.walletAddress = null;
};
</script>
