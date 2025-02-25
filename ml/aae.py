import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

import warnings
warnings.filterwarnings(action="ignore")


class Encoder(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(Encoder, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),

            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2),

            nn.Linear(256, latent_dim)
        )

    def forward(self, x):
        return self.model(x)


class Decoder(nn.Module):
    def __init__(self, latent_dim, output_dim):
        super(Decoder, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2),

            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),

            nn.Linear(512, output_dim),
            nn.Tanh()
        )

    def forward(self, z):
        return self.model(z)


class Discriminator(nn.Module):
    def __init__(self, latent_dim):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),

            nn.Linear(256, 128),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),

            nn.Linear(128, 1),
            nn.Sigmoid()
        )

    def forward(self, z):
        return self.model(z)


def reduce_embedding_aae(embedding, latent_dim=256, num_epochs=1000, batch_size=64, lr=0.0002):
    """
    :param embedding: numpy.ndarray, shape (num_samples, high_dim)
    :param latent_dim: 目标潜在空间维度
    :param num_epochs: 训练轮数
    :param batch_size: 批量大小
    :param lr: 学习率
    :return: numpy.ndarray, shape (num_samples, latent_dim)
    """
    if not isinstance(embedding, np.ndarray):
        raise ValueError("embedding should be numpy.ndarray")

    num_samples, high_dim = embedding.shape
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    embedding_tensor = torch.tensor(embedding, dtype=torch.float32).to(device)

    encoder = Encoder(high_dim, latent_dim).to(device)
    decoder = Decoder(latent_dim, high_dim).to(device)
    discriminator = Discriminator(latent_dim).to(device)

    optim_AE = optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=lr)
    optim_D = optim.Adam(discriminator.parameters(), lr=lr)

    criterion_ae = nn.MSELoss()
    criterion_gan = nn.BCELoss()

    real_label, fake_label = 1, 0

    for epoch in tqdm(range(num_epochs), desc='Training AAE'):
        idx = np.random.randint(0, num_samples, batch_size)
        real_data = embedding_tensor[idx]

        optim_AE.zero_grad()
        z = encoder(real_data)
        reconstructed_data = decoder(z)
        ae_loss = criterion_ae(reconstructed_data, real_data)
        ae_loss.backward()
        optim_AE.step()

        optim_D.zero_grad()
        real_z = torch.randn(batch_size, latent_dim).to(device)
        fake_z = encoder(real_data).detach() 

        real_output = discriminator(real_z)
        fake_output = discriminator(fake_z)

        real_loss = criterion_gan(real_output, torch.ones_like(real_output) * real_label)
        fake_loss = criterion_gan(fake_output, torch.zeros_like(fake_output) * fake_label)
        d_loss = real_loss + fake_loss
        d_loss.backward()
        optim_D.step()

        optim_AE.zero_grad()
        fake_z = encoder(real_data)
        fake_output = discriminator(fake_z)
        g_loss = criterion_gan(fake_output, torch.ones_like(fake_output) * real_label)
        g_loss.backward()
        optim_AE.step()

    with torch.no_grad():
        reduced_embedding = encoder(embedding_tensor).cpu().numpy()

    return reduced_embedding